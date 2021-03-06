package com.codingdojo.dojosninjas.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.dojosninjas.models.Dojo;
import com.codingdojo.dojosninjas.repositories.DojoRepo;

@Service
public class DojoService {
	
	private final DojoRepo dojoRepo;

	public DojoService(DojoRepo dojoRepo) {
		this.dojoRepo = dojoRepo;
	}

	public List<Dojo> getAllDojos() {
		return (List<Dojo>) dojoRepo.findAll();
	}

	public Dojo createDojo(Dojo dojo) {
		return dojoRepo.save(dojo);
	}

	public Dojo findDojoById(Long id) {
		Optional<Dojo> findDojo = dojoRepo.findById(id);
		if (findDojo.isPresent()) {
			return findDojo.get();
		} else {
			return null;
		}
	}
}